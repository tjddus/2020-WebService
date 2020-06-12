<template>
  <div class="text-right">
    <v-dialog
      v-model="dialog"
      width="500"
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
          사업자가 약관을 내용으로 하여 고객과 계약을 체결한 후 「약관의 규제에 관한 법률」 위반 여부가 문제되는 약관조항을 수정·삭제하여 수정된 약관조항에 따라 새로운 고객과 계약을 체결하게 되었으나 종전의 고객에 대하여는 계약의 내용을 수정하지 아니하는 경우,
          종전의 약관조항이 동법 제19조에 의하여 동법 위반 여부에 대한 심사청구의 대상이 되는지 여부
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    name: "ProductTestForm",
    props:{
      dialog: Boolean
    },
    data() {
      return {
      }
    }
  }
</script>

<style scoped>

</style>
