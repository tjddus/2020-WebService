<template>
  <div>
    <v-dialog
      v-model="sdialog"
      max-width="400px">
      <v-card>
        <v-card-title>
          <p class="title font-weight-light">심사 평가</p>
        </v-card-title>
        <v-form class="px-3" v-model="valid" @submit.prevent="createTester">
          <v-card-text>
            <v-text-field
              outlined
              label="심사 등급"
              v-model="grade"
              color="blue"
            />
            <v-text-field
              outlined
              label="심사 평가 내용"
              v-model="content"
              color="blue"
            />
          </v-card-text>
          <v-card-actions>
            <v-spacer/>
            <v-btn
              depressed
              class="mr-3 mb-3 text-lowercase font-weight-light"
              type="submit"
              @click="dialog = false">
              제출
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
    <product-test-check-component :tdialog="tdialog" :grade="grade"/>
  </div>
</template>

<script>
  import ProductTestCheckComponent from "./ProductTestCheckComponent";

  export default {
    name: "ProductTestFormComponent",
    data() {
      return {
        valid: false,
        grade: null,
        content: null,
        rules: {
          grade: v => v >= 0 || 'Loan should be above £5000',
          grade: v => v <= 10 || 'Max should not be above £50,000',
          content: v => !!v || '심사 평가 내용을 작성해주세요'
        },
        tdialog: false
      }
    },
    components: {
      ProductTestCheckComponent
    },
    props: {
      sdialog: Boolean,
      productId: Number,
    },
    methods: {
      clearTester() {
        this.grade = null
      },

      async createTester() {
        try {
          await this.$store.dispatch('tester/createTester', {
            grade: this.grade,
            content: this.content,
            productId: this.productId
          });
          this.clearTester();
          this.sdialog = false;
          this.tdialog = true;
        } catch (e) {
          console.error(e);
        }
      }
    }
  }
</script>

<style scoped>

</style>
