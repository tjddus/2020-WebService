<template>
  <v-row>
    <div @click="showSingleProduct(product.id)">
      <v-card
        :loading="loading"
        class="my-2 ml-10"
        max-width="300"
        max-height="600"
      >
        <v-img
          height="200"
          :src="product.photoUrl"
        ></v-img>

        <v-card-title class="subtitle-1">{{product.name}}</v-card-title>

        <v-card-text>
          <div class="caption">
            <div v-if="product.publishedYn">
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
        <v-card-text v-if="!product.publishedYn">
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
        </v-card-text>
      </v-card>
    </div>
  </v-row>
</template>


<script>

  export default {
    name: "ProductCardComponent",
    data() {
      return {
        loading: false,
        selection: 1,
        productId: String(this.product.id)
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
    },

  }
</script>

<style scoped>

</style>
