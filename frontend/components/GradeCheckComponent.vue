<template>
  <div class="text-right">
    <v-dialog
      v-model="gdialog"
      width="400"
    >
      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          심사 평가 등급
        </v-card-title>

        <v-card-text class="subtitles-2 font-weight-bold">
          <br>
          {{grade}}
        </v-card-text>

        <v-divider></v-divider>


        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="acceptGradeCheck"
          >
            I agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    name: "GradeCheckComponent",
    props: {
      gdialog: Boolean,
      productId: Number,
    },
    computed: {
      product() {
        return this.$store.state.product.product
      },
      testers() {
        return this.$store.state.tester.testers
      },
      grade() {
        var total = 0;
        for (var i = 0; i < this.testers.length; i++) {
          total = total + this.testers[i].grade
        }
        return total
      }
    },
    methods: {
      acceptGradeCheck() {
        this.gdialog = false;
      }
    },
    async created() {
      await this.$store.dispatch('tester/loadTesters', {productId: this.productId})
    }
  }
</script>

<style scoped>

</style>
