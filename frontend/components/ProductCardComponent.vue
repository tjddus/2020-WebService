<template>
  <v-row>
    <div @click="showSingleProduct">
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
      >
        <v-img
          height="250"
          :src="product.photoUrl"
        ></v-img>

        <v-card-title>{{product.name}}</v-card-title>

        <v-card-text>
          <v-row
            align="center"
            class="mx-0"
          >
            <v-rating
              :value="4.5"
              color="amber"
              dense
              half-increments
              readonly
              size="14"
            ></v-rating>

            <div class="grey--text ml-4">4.5 (413)</div>
          </v-row>

          <div class="my-4 subtitle-1">
            <div v-if="product.publishedYn">
              심사중
            </div>
            <div v-else>
              {{product.createdDate}}
            </div>
          </div>

          <div>{{product.createdDate}}</div>
          <div>{{product.category}}</div>
          <div>{{product.makerName}}</div>
        </v-card-text>

        <v-divider class="mx-4"></v-divider>

        <v-card-title>Tonight's availability</v-card-title>

        <v-card-text>
          <v-chip-group
            v-model="selection"
            active-class="deep-purple accent-4 white--text"
            column
          >
            <v-chip>5:30PM</v-chip>

            <v-chip>7:30PM</v-chip>

            <v-chip>8:00PM</v-chip>

            <v-chip>9:00PM</v-chip>
          </v-chip-group>
        </v-card-text>

        <v-card-actions>
          <v-btn
            color="deep-purple lighten-2"
            text
            @click="reserve"
          >
            Reserve
          </v-btn>
        </v-card-actions>
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
        // productId: String(this.product.id)
      }
    },
    props: {
      product: Object
    },

    methods: {
      reserve() {
        this.loading = true;

        setTimeout(() => (this.loading = false), 2000)
      },
      showSingleProduct(productId) {
        this.$router.push(`post/${productId}`);
      },
      Amount() {
        return int(this.product.totalAmount / this.product.totalSupporter)
      }

    },

  }
</script>

<style scoped>

</style>
