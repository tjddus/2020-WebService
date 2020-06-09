from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import json
from products.models import Product, Tester, Comment
from django.contrib.auth.models import User
from products.serializers import ProductSerializer, CommentSerializer, TesterSerializer, CreateProductSerializer


class loadProducts(generics.GenericAPIView):
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
#         publishedYn = request.GET.get('publishedYn')
#         queryset = Product.objects.filter(publishedYn = publishedYn)
        queryset = Product.objects.all()
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


## Tester 기능
@api_view(['POST'])
def createTester(request, productId):
    '''
    상품 테스터에 유저 추가
    ---
    ## `/product/createTester/{productId}`
    '''
    permissions_classes=[
        permissions.IsAuthenticated,
    ]
    if request.method == 'POST':
        try:
            Tester.objects.get(product=productId, user=self.request.user.id)
            return Response("이미 존재하는 유저입니다")
        except:
            user = User.objects.get(id=self.request.user.id)
            product = Product.objects.get(id=productId)
            grade = request.data.get('grade')

            tester = Tester.objects.create(
                product=product, user=user, grade=grade
            )
            print(tester)
            return Response(tester)
    else:
        raise NameError

@api_view(['DELETE'])
def deleteTester(request, productId):
    '''
    상품 테스터에 유저 삭제
    ---
    ## `/product/deleteTester/{productId}`
    '''
    permissions_classes=[
        permissions.IsAuthenticated,
    ]
    if request.method == 'DELETE':
        tester = Tester.objects.get(post=productId, user=self.request.user.id)

        tester.delete()
        return Response("delete success")
    else:
        raise NameError


@api_view(['GET'])
def loadTesters(request, productId):
    '''
    상품 테스터에 대한 전체 등급 선정을 위한 조회
    ---
    ## `/product/loadTester/{productId}`
    '''
    queryset = Tester.objects.all().order_by('-id')
    queryset = queryset.filter(id = productId)
    testers = []
    for query in queryset:
        tester = {}
        tester['id'] = query.id
        tester['user'] = query.user
        tester['grade'] = query.user.username
        tester['createdAt'] = query.createdAt
        testers.append(tester)
    return Response(testers)



class loadComments(generics.GenericAPIView):
    def get(self, request, productId, *args, **kwargs):
        print(productId)
        queryset = Comment.objects.filter(product=productId)
        comments = CommentSerializer(queryset, many=True).data
        print(comments)
        return Response({"comments" : comments})



## Comment 기능
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
        try:
            Comment.objects.get(product=productId, user=self.request.user.id)
            return Response("이미 존재하는 유저입니다")
        except:
             user = User.objects.get(id=self.request.user.id)
             product = Product.objects.get(id=productId)
             content = request.data.get('content')

             comment = Comment.objects.create(
                    product=product, user=user, content=content
                )
             print(comment)
             return Response(comment)
        else:
            raise NameError

@api_view(['DELETE'])
def deleteComment(request, commentId):
    '''
    상품 댓글에 유저 추가 및 삭제
    ---
    ## `/product/deleteComment/{commentId}`
    '''
    permissions_classes=[
        permissions.IsAuthenticated,
    ]
    if request.method == 'DELETE':
        comment = Comment.objects.get(id = commentId)

        comment.delete()
        return Response("delete success")
    else:
        raise NameError
