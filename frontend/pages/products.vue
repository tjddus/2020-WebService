<template>
  <v-row>
    <div v-if="products !== null">
      <v-col cols="3" v-for="(product, index) in products" :key="index">
        <product-card-component :product="product" class="card"/>
      </v-col>
    </div>
    <v-col cols="12">
      <post-form-component/>
    </v-col>
  </v-row>
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
      await this.$store.dispatch('product/loadProducts');
    },
  }
</script>

<style scoped>

</style>
