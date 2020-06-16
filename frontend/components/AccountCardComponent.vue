<template>
  <v-card outlined>
    <v-form v-model="valid" @submit.prevent="">
      <v-card-text>
        <v-row>
          <v-col sm="2">
            <v-subheader class="caption">이름</v-subheader>
          </v-col>
          <v-col sm="6">
            <v-text-field
              v-model="me.username"
              :rules="[rules.name]"
              label="이름"
              outlined
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col sm="2">
            <v-subheader class="caption">이메일</v-subheader>
          </v-col>
          <v-col sm="6">
            <v-text-field
              v-model="me.email"
              :rules="[rules.email]"
              label="이메일"
              outlined
            ></v-text-field>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer/>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
  export default {
    name: 'AccountCardComponent',
    data() {
      return {
        valid: true,
        email: '',
        username: '',
        password: '',
        rules: {
          email: v => (v || '').match(/@/) || '유효한 이메일을 입력해주세요.',
          name: v => !!v || '이름을 입력해주세요.',
          password: v => !!v || '비밀번호를 입력해주세요.',
        }
      }
    },
    computed: {
      me() {
        return this.$store.state.user.me
      }
    }
  }
</script>
