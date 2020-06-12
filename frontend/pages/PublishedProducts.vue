<template>
  <v-container>
    <v-layout row justify-center="center">
      <div v-for="(product, index) in products">
        <v-flex md4 v-if="index % 3 === 0">
          <product-card-component :product="product"/>
        </v-flex>
        <v-flex md4 v-if="index % 3 === 1">
          <product-card-component :product="product"/>
        </v-flex>
        <v-flex md4 v-if="index % 3 === 2">
          <product-card-component :product="product"/>
        </v-flex>
      </div>
    </v-layout>
  </v-container>
</template>

<script>
  import ProductCardComponent from "../components/ProductCardComponent";

  export default {
    name: "products",
    components: {
      ProductCardComponent
    },
    computed: {
      products() {
        return this.$store.state.product.products;
      }
    },
    async created() {
      //상품 전부 로딩
      console.log('products created');
      await this.$store.dispatch('product/loadPublishedProducts');
    },
  }
</script>

<style scoped>

</style>
