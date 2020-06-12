<template>
  <div class="text-right">
    <v-dialog
      v-model="tdialog"
      width="400"
    >
      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          심사 평가 확인
        </v-card-title>

        <v-card-text>
          심사 평가 완료하였습니다.
        </v-card-text>

        <v-divider></v-divider>


        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="acceptCheck"
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
    name: "ProductTestCheckComponent",
    props: {
      tdialog: Boolean,
      grade: Number
    },
    methods: {
      acceptCheck() {
        this.tdialog = false;
      }
    },
  }
</script>

<style scoped>

</style>
