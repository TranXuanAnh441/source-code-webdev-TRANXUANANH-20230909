<template>
  <section>
    <div class="container">
      <div class="row">
        <div class="col-lg-5">
          <h1 class="mb-3"><strong>Register now</strong></h1>
          <form @submit.prevent="submit">
            <div v-if="errors.length">
              <ul>
                <li v-for="error in errors" class="text-danger">{{ error }}</li>
              </ul>
            </div>
            <div class="mb-3">
              <label for="username" class="form-label">User Name:</label>
              <input type="text" name="username" v-model="user.username" class="form-control" />
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Email:</label>
              <input type="text" name="email" v-model="user.email" class="form-control" />
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password:</label>
              <input type="password" name="password" v-model="user.password" class="form-control" />
            </div>
            <div class="mb-3">
              <label for="passwordConfirm" class="form-label">Password confirm:</label>
              <input type="password" name="passwordConfirm" v-model="user.passwordConfirm" class="form-control" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
        <HeroImage />
      </div>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';
import HeroImage from '@/components/HeroImage.vue';

export default defineComponent({
  name: 'Register',
  components: {
    HeroImage
  },
  data() {
    return {
      errors: [],
      user: {
        username: '',
        email: '',
        role: 'user',
        photo: 'default',
        password: '',
        passwordConfirm: '',
        verified: false,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      let router = this.$router;
      this.errors = [];

      if (!this.user.username) {
        this.errors.push('Username required.');
      }
      if (!this.user.email) {
        this.errors.push('Email required.');
      }
      if (!this.user.password) {
        this.errors.push('Password required.');
      }
      if (!this.user.passwordConfirm) {
        this.errors.push('Password confirm required.');
      }

      if (this.errors.length > 0) {
        return false;
      }

      try {
        await this.register(this.user).then(
          function response() {
            router.push('/login');
          }
        );
      } catch (error) {
        this.errors.push(error.response.data.detail);
      }
    },
  },
});
</script>