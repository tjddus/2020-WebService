<template>
  <div class="text-right">
    <v-dialog
      v-model="dialog"
      width="600"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          심사참여
        </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          Privacy Policy
        </v-card-title>

        <v-card-text>
          현 회사는 개인정보보호에 따 취급하는 모든 개인정보는 관련 법령에 근거하여 수집 · 보유 및 처리되고 있습니다. 「개인정보보호법」은 이러한 개인정보의 취급에 대한 일반적 규범을 제시하고 있으며, 현
          회사는 이러한 법령의 규정에 따라 수집 · 보유 및 처리하는 개인정보를 공공업무의 적절한 수행과 이용자의 권익을 보호하기 위해 적법하고 적정하게 취급할 것입니다.

          또한,현 회사는 관련 법령에서 규정한 바에 따라 보유하고 있는 개인정보에 대한 열람, 정정·삭제, 처리정지 요구 등 이용자의 권익을 존중하며, 이용자는 이러한 법령상 권익의 침해 등에 대하여
          행정심판법에서 정하는 바에 따라 행정심판을 청구할 수 있습니다.

          현 회사는 개인정보보호법 제 30조에 따라 정보주체의 개인정보 보호 및 권익을 보호하고 개인정보와 관련한 이용자의 고충을 원활하게 처리할 수 있도록 다음과 같은 개인정보 처리방침을 수립 · 공개하고
          있습니다.
        </v-card-text>

        <v-divider></v-divider>


        <v-card-actions>
          <v-checkbox
            v-model="checkbox"
            :label="`개인정보 약관에 동의합니다`"
          ></v-checkbox>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="acceptPrivacy"
          >
            I accept
          </v-btn>
        </v-card-actions>

        <product-test-form-component :sdialog="sdialog" :productId="productId"/>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  import ProductTestFormComponent from "./ProductTestFormComponent";

  export default {
    name: "AcceptPrivacyComponent",
    props: {
      dialog: Boolean,
      productId: Number,
    },
    components: {
      ProductTestFormComponent
    },
    data() {
      return {
        checkbox: false,
        sdialog: false,
      }
    },
    methods: {
      acceptPrivacy() {
        if (this.checkbox === true) {
          this.dialog = false;
          this.sdialog = true;
        }
      }
    },
  }
</script>

<style scoped>

</style>
