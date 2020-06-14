<template>
  <v-layout justify-center="center" align-center="center" class="my-10">
    <v-flex
      xs12 md10>
      <div>
        <v-row no-gutters>
          <v-col col="9">
            <v-row>
              <v-col cols="12">
                <img :src="product.photoUrl" width="610px" class="border 1px darkgrey;">
              </v-col>
              <div class="pa-6">
                <v-col cols="12">
                  <h1 class="title text-left font-weight-bold">{{product.name}}</h1>
                </v-col>
                <v-col cols="12">
                  <div class="subtitle-2 grey--text">{{product.makerName}}</div>
                </v-col>
              </div>
            </v-row>
          </v-col>
          <v-col col="3" class="pa-8">
            <v-row>
              <v-col cols="12" class="font-weight-bold">
                <h2 styl="title">남은 시간 <span class="blue--text text--darken-4">"{{endTime}}"</span>일</h2>
              </v-col>
              <v-progress-linear
                color="primary"
                height="3"
                reactive
              ></v-progress-linear>
              <v-col cols="12" class="subtitle-2 font-weight-normal">
                카테고리<span class="title font-weight-bold">&nbsp; {{product.category}}</span>
              </v-col>
              <v-col cols="12" class="subtitle-2 font-weight-normal">
                펀딩률<span class="title font-weight-bold">&nbsp; {{product.achievementRate}}</span> %
              </v-col>
              <v-col cols="12" class="subtitle-2 font-weight-normal">
                가격<span class="title font-weight-bold">&nbsp; {{amount}}</span> 원
              </v-col>
              <v-col cols="12" class="subtitle-2 font-weight-normal">
                서포터수<span class="title font-weight-bold">&nbsp; {{product.totalSupporter}}</span> 명
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <comment-card-component/>
        <comment-form-component :productId="product.id"/>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
  import CommentFormComponent from "../../components/CommentFormComponent";
  import CommentCardComponent from "../../components/CommentCardComponent";
  import moment from 'moment';

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
      endTime() {
        var momentObj = moment(this.product.createdDate);
        var momentObj = momentObj.add('30', 'days').subtract(moment(new Date()));
        var endTime = momentObj.format('DD');
        return endTime
      },
      amount() {
        return parseInt(this.product.totalAmount / this.product.totalSupporter);
      }
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
