<template>
  <div>
    <div  align="center">
      <v-icon small color="red darken-2">adjust</v-icon>
      펀딩 종료 &nbsp;
      <v-icon small color="yellow darken-2">adjust</v-icon>
      펀딩 심사중 &nbsp;
      <v-icon small color="green darken-2">adjust</v-icon>
      펀딩 진행중 &nbsp;
    </div>
    <product-data-table-component/>
  </div>
</template>

<script>
  import ProductDataTableComponent from "../components/ProductDataTableComponent";

  export default {
    name: "allProducts",
    components: {
      ProductDataTableComponent
    },
    async created() {
      //상품 전부 로딩
      console.log('products created');
      await this.$store.dispatch('product/loadAllProducts');
    },
  }
</script>

<style scoped>

</style>

