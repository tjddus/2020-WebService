<template>
  <div>
    <v-row no-gutters
           justify="center">
      <v-col col="6">
        <v-row class="my-10">
          <v-col cols="12">
            <img :src="product.photoUrl" width="90%" class="border 1px darkgrey;">
          </v-col>
          <v-col cols="12">
            <div class="title font-weight-bold">{{product.name}}</div>
          </v-col>
          <v-col cols="12">
            {{product.makerName}}
          </v-col>
        </v-row>
      </v-col>
      <v-col col="3">
        <v-row>
          <v-col cols="12">
            {{product.category}}
          </v-col>
          <v-col cols="12">
            {{product.achievementRate}}
          </v-col>
          <v-col cols="12">
            {{product.totalAmount}}
          </v-col>
          <v-col cols="12">
            {{product.totalSupporter}}
          </v-col>
          <v-col cols="12">
            {{time}}
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-btn @click.prevent="deleteProduct">삭제</v-btn>
    <comment-form-component :productId="product.id"/>
    <v-row v-if="comments.length !== 0">
      <v-col cols="3">아이디</v-col>
      <v-col cols="5">댓글</v-col>
      <v-col cols="2">수정</v-col>
      <v-col cols="2">삭제</v-col>
      <v-col cols="12" v-for="(comment, index) in comments" :key="index">
        <comment-card-component :comment="comment"/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import CommentFormComponent from "../../components/CommentFormComponent";
  import CommentCardComponent from "../../components/CommentCardComponent";

  export default {
    name: "_productId",
    components: {
      CommentFormComponent,
      CommentCardComponent
    },
    computed: {
      product() {
        return this.$store.state.product.product;
      },
      comments() {
        return this.$store.state.comment.comments;
      },
      time() {
        return this.$moment(this.product.createdAt).fromNow();
      },
    },

    async fetch({store, params}) {
      await store.dispatch('product/loadProduct', {productId: params.productId});
      await store.dispatch('comment/loadComments', {productId: params.productId});
    },
    methods: {
      backProduct() {
        return this.$router.go(-1);
      },
      async deleteProduct() {
        try {
          console.log(this.product.id);
          await this.$store.dispatch('product/deleteProduct', {productId: this.product.id});
          return this.$router.replace('/products');
        } catch (e) {
          console.error(e);
        }
      },
    }
  }
</script>

<style scoped>

</style>
