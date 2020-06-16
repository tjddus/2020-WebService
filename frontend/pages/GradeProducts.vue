<template>
  <div>
    <grade-data-table-component/>
  </div>
</template>

<script>
  import GradeDataTableComponent from "../components/GradeDataTableComponent";

  export default {
    name: "GradeProducts",
    async created() {
      //상품 전부 로딩
      console.log('products created');
      await this.$store.dispatch('tester/loadAllTesters');
    },
    components: {
      GradeDataTableComponent
    }
  }
</script>

<style scoped>

</style>
