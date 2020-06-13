<template>
  <v-layout justify-center="center" class="my-10">
    <v-flex xs12 md10>
      <v-toolbar-title class="font-weight-bold">상품 모니터링</v-toolbar-title>
      <v-data-table
        :headers="headers"
        :items="products"
        :pagination.sync="pagination"
        hide-actions>
        <template v-slot:item.type="{item}">
          <div v-if="item.publishedYn === true && item.endYn === true">
            <v-btn icon>
              <v-icon color="red darken-2">adjust</v-icon>
            </v-btn>
          </div>
          <div v-if="item.publishedYn === true && item.endYn === false">
            <v-btn icon>
              <v-icon color="green darken-2">adjust</v-icon>
            </v-btn>
          </div>
          <div v-if="item.publishedYn === false && item.endYn === true">
            <v-btn icon>
              <v-icon color="yellow darken-2">adjust</v-icon>
            </v-btn>
          </div>
          <div v-if="item.publishedYn === false && item.endYn === false">
            <v-btn icon>
              <v-icon color="yellow darken-2">adjust</v-icon>
            </v-btn>
          </div>
        </template>


        <template v-slot:item.actions="{ item }">
          <v-icon
            small
            class="mr-2"
            @click="editProduct(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="deleteProduct(item)"
          >
            mdi-delete
          </v-icon>
        </template>
      </v-data-table>
    </v-flex>
  </v-layout>

</template>

<script>
  import 'material-design-icons-iconfont/dist/material-design-icons.css'

  export default {
    name: 'ProductDataTableComponent',
    data() {
      return {
        pagination: {},
        headers: [
          {text: '타입', value: 'type', width: '50px'},
          {text: '이름', align: 'left', sortable: 'false', value: 'name', width: '150px'},
          {text: '메이커', value: 'makerName', width: '100px'},
          {text: '심사완료', value: 'publishedYn', width: '30px'},
          {text: '액션', value: 'actions', width: '30px'}
        ],
      }
    },
    computed: {
      products() {
        return this.$store.state.product.products
      }
    },
    methods: {
      async deleteProduct(item) {
        try {
          console.log(item.id);
          await this.$store.dispatch('product/deleteProduct', {productId: item.id});
        } catch (e) {
          console.error(e);
        }
      },
      async editProduct(item) {
        try {
          console.log(item.id);
          await this.$store.dispatch('product/editProduct', {productId: item.id});
        } catch (e) {
          console.error(e);
        }
      }
    }
  }
</script>
