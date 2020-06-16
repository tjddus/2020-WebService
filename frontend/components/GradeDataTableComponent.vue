<template>
  <v-layout justify-center="center" class="my-10">
    <v-flex xs12 md10>
      <v-toolbar-title class="font-weight-bold">개별 등급 모니터링</v-toolbar-title>
      <v-data-table
        :headers="headers"
        :items="allProductsTesters"
        :pagination.sync="pagination"
        hide-actions>
      </v-data-table>
    </v-flex>
  </v-layout>
</template>

<script>
  import 'material-design-icons-iconfont/dist/material-design-icons.css'

  export default {
    name: 'GradeDataTableComponent',
    data() {
      return {
        pagination: {},
        headers: [
          {text: '이름', align: 'left', sortable: 'false', value: 'name', width: '150px'},
          {text: '메이커', value: 'makerName', width: '100px'},
          {text: '테스터 아이디', value: 'testerId', width: '100px'},
          {text: '심사점수', value: 'grade', width: '30px'},
        ],
      }
    },
    computed: {
      allProductsTesters() {
        return this.$store.state.tester.allProductsTesters
      },
    },
    methods: {}
  }
</script>
