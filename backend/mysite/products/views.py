from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import json
from products.models import Product, Tester, Comment
from django.contrib.auth.models import User
from products.serializers import ProductSerializer, CommentSerializer, TesterSerializer, CreateProductSerializer

class loadAllProducts(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        products = ProductSerializer(queryset, many=True).data
        return Response({'products': products})

class loadPublishedProducts(generics.GenericAPIView):
    '''
    상품 전체 조회 페이지
    ---
    ## `/product/loadProducts`
    ## 내용
        - pid: 상품 아이디
        - name: 상품 이름
        - category: 카테고리 분류
        - makerName: 메이커 이름
        - photoUrl: 이미지
        - createdDate: 생성 날짜
        - publishedYn: 게시 유무 // 펀딩 중 : 심사 중
        - achievementRate: 성취
        - totalAmount: 전체 금
        - totalSupporter: 서포터
        - totalLike: 전체 좋아요 수
        - endYn: 펀딩 종료
        - detailUrl: 상세 주
    '''
    def get(self, request, *args, **kwargs):
        products = []
        queryset = Product.objects.filter(publishedYn = True)
#         queryset = Product.objects.all()
        print(queryset)
        products = ProductSerializer(queryset, many=True).data
        return Response({'products': products})



class loadNotPublishedProducts(generics.GenericAPIView):
    '''
    상품 전체 조회 페이지
    ---
    ## `/product/loadProducts`
    ## 내용
        - pid: 상품 아이디
        - name: 상품 이름
        - category: 카테고리 분류
        - makerName: 메이커 이름
        - photoUrl: 이미지
        - createdDate: 생성 날짜
        - publishedYn: 게시 유무 // 펀딩 중 : 심사 중
        - achievementRate: 성취
        - totalAmount: 전체 금
        - totalSupporter: 서포터
        - totalLike: 전체 좋아요 수
        - endYn: 펀딩 종료
        - detailUrl: 상세 주
    '''
    def get(self, request, *args, **kwargs):
        products = []
        queryset = Product.objects.filter(publishedYn = False)
#         queryset = Product.objects.all()
        print(queryset)
        products = ProductSerializer(queryset, many=True).data
        return Response({'products': products})

class loadProduct(generics.GenericAPIView):
    '''
    상품 상세 조회 페이지
    ---
    ## `/product/productDetail/<int:pk>`
    '''
    def get(self, request, productId):
        queryset = Product.objects.get(id=productId)
        print(queryset)
        product = ProductSerializer(queryset).data
        return Response({'product': product})

class deleteProduct(generics.GenericAPIView):
    '''
    상품 삭제 페이지
    ---
    ## `/product/deleteProduct/<int:productId>`
    '''
    def delete(self, request, productId, *args, **kwargs):
        product = Product.objects.get(id=productId)
        product.delete()
        return Response({'info': 'Database deleted'})

class editProduct(generics.GenericAPIView):
     '''
     상품 삭제 페이지
     ---
     ## `/product/deleteProduct/<int:productId>`
     '''
     def get(self, request, productId, *args, **kwargs):
        queryset = Product.objects.get(id = productId)
        queryset.publishedYn = True
        queryset.save()
        print(queryset)
        newProduct = ProductSerializer(queryset).data
        return Response({'newProduct': newProduct})


class loadTesters(generics.GenericAPIView):
    '''
    상품 테스터에 대한 전체 등급 선정을 위한 조회
    ---
    ## `/product/loadTester/{productId}`
    '''
    def get(self, request, productId, *args, **kwargs):
        print(productId)
        queryset = Tester.objects.filter(product=productId).order_by('user')
        testers = TesterSerializer(queryset, many = True).data
        print(testers)
        return Response({'testers': testers})


class createTester(generics.GenericAPIView):
    '''
    상품 테스터에 유저 추가
    ---
    ## `/product/createTester/{productId}`
    '''
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    def post(self, request, productId, *args, **kwargs):
        try:
            Tester.objects.get(product=productId, user=self.request.user.id)
            return Response('이미 존재하는 유저이다')
        except:
            user = User.objects.get(id = self.request.user.id)
            product = Product.objects.get(id = productId)
            grade = request.data.get('grade')
            content = request.data.get('content')

            tester = Tester.objects.create(
                product = product, user=user, grade=grade, content=content
            )
            tester = TesterSerializer(tester).data
            return Response({'tester': tester})

class deleteTesters(generics.GenericAPIView):
    '''
    상품 테스터에 유저 삭제
    ---
    ## `/product/deleteTester/{productId}`
    '''
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    def delete(self, request, *args, **kwargs):
        tester = Tester.objects.filter(product=productId)
        tester.delete()
        return Response("Database deleted!")

## Comment 로드
class loadComments(generics.GenericAPIView):
    def get(self, request, productId, *args, **kwargs):
        print(productId)
        queryset = Comment.objects.filter(product=productId)
        comments = CommentSerializer(queryset, many=True).data
        print(comments)
        return Response({"comments" : comments})

## Comment 생성
class createComment(generics.GenericAPIView):
    '''
    상품 댓글에 유저 추가 및 삭제
    ---
    ## `/product/createComment/{productId}`
    '''
    permissions_classes=[
        permissions.IsAuthenticated,
    ]
    def post(self, request, productId, *args, **kwargs):
        print(self.request.data, productId)
        print(self.request.user)
        user = User.objects.get(id=self.request.user.id)
        product = Product.objects.get(id=productId)
        content = request.data.get('content')
        print(content, user, product)
        comment = Comment.objects.create(
                    product=product, user=user, content=content
        )
        comment = CommentSerializer(comment).data
        return Response({'comment': comment})


class updateComment(generics.GenericAPIView):
    '''
    상품 댓글 수정
    ---
    ## `/product/updateComment/<int:commentId>`
    '''
    permissions_classes = [
        permissions.IsAuthenticated
    ]
    def post(self, request, commentId, *args, **kwargs):
        print(request.data)
        newContent = request.data.get('newContent')

        queryset = Comment.objects.get(id=commentId)
        queryset.content = newContent
        queryset.save()
        print(queryset)
        updatedComment = CommentSerializer(queryset).data
        return Response({'updatedComment': updatedComment})

## comment 삭제
class deleteComment(generics.GenericAPIView):
    '''
    상품 댓글 삭제
    ---
    ## `/product/deleteComment/<int:commentId>`
    '''
    def delete(self, request, commentId, *args, **kwargs):
        comment = Comment.objects.get(id=commentId)
        comment.delete()
        return Response({'info': 'Database deleted'})