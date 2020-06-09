<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="2">
          {{comment.user.userName}}
        </v-col>
        <v-col cols="6">
          <v-text-field v-if="updateTrue"
                        v-model="newComment">
          </v-text-field>
          <div v-if="!updateTrue" @click="updateCommentTrue">
            {{comment.comment}}
          </div>
        </v-col>

        <v-col cols="2">
          <v-btn icon @click.prevent="updateComment">
            <v-icon>mdi-update</v-icon>
          </v-btn>
        </v-col>
        <v-col cols="2">
          <v-btn icon @click="deleteComment">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  export default {
    name: "CommentCardComponent",
    data() {
      return {
        updateTrue: false,
        newComment: this.comment.comment
      }
    },
    props: {
      comment: Object
    },
    methods: {
      async deleteComment() {
        try {
          await this.$store.dispatch('comment/deleteComment', {
            comment: this.comment
          });
        } catch (e) {
          console.error(e);
        }
      },
      updateCommentTrue() {
        this.updateTrue = !this.updateTrue;
        this.newComment = this.comment.comment;
        console.log('click updateComment');
      },
      async updateComment() {
        try {
          await this.$store.dispatch('comment/updateComment', {
            comment: this.comment,
            newComment: this.newComment
          });
          this.newComment = this.comment.comment;
          this.updateTrue = false;
        } catch (e) {
          console.error(e);
        }
      }
    }
  }
</script>

<style scoped>

</style>
