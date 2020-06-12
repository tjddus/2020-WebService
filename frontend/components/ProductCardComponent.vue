<template>
  <v-row>
    <v-card
      :loading="loading"
      class="my-2 ml-10"
      max-width="300"
      max-height="600"
    >
      <div @click="showSingleProduct(product.id)">
        <v-img
          height="200"
          :src="product.photoUrl"
        ></v-img>

        <v-card-title class="subtitle-1">{{product.name}}</v-card-title>

        <v-card-text>
          <div class="caption">
            <div v-if="!product.publishedYn">
              심사중
            </div>
            <div v-else>
              {{amount}}
            </div>
          </div>

          <div>{{time}}</div>
          <div>{{product.category}}</div>
          <div>{{product.makerName}}</div>
        </v-card-text>

        <v-divider class="mx-4"></v-divider>
      </div>
      <v-card-text v-if="product.publishedYn">
        <v-progress-linear
          v-model="product.achievementRate"
          color="primary"
          height="25"
          reactive
        >
          <template v-slot="{ value }">
            <strong>{{ Math.ceil(value) }}%</strong>
          </template>
        </v-progress-linear>
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          text
          @click="checkGrade"
        >
          등급 확인
        </v-btn>
      </v-card-text>
      <v-card-text v-else>
          <accept-privacy-component :dialog="dialog" :productId="productId"/>
      </v-card-text>
    </v-card>
  </v-row>
</template>


<script>
  import AcceptPrivacyComponent from "./AcceptPrivacyComponent";

  export default {
    name: "ProductCardComponent",
    components: {
      AcceptPrivacyComponent
    },
    data() {
      return {
        loading: false,
        selection: 1,
        productId: String(this.product.id),
        dialog: false
      }
    },
    props: {
      product: Object
    },
    computed: {
      time() {
        return this.$moment(this.product.createdAt).fromNow()
      },
      amount() {
        return parseInt(this.product.totalAmount / this.product.totalSupporter)
      },
    },
    methods: {
      showSingleProduct(productId) {
        this.$router.push(`product/${productId}`);
      },
      createTester(productId) {
        this.dialog = true;
        this.$store.dispatch('product/createTester');
      }
    },

  }
</script>

<style scoped>

</style>
