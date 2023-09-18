<template>
  <section>
    <div class="container">
      <div class="row">
        <div class="col-lg-5">
          <h1 class="mb-3"><strong>Login now</strong></h1>
          <h5>Or register new account <router-link :to="{ name: 'Register' }">here</router-link></h5>
          <form @submit.prevent="submit">
            <div v-if="form.errors.length" class="text-danger">
              Please fix the errors below:
              <ul>
                <li v-for="error in form.errors">{{ error }}</li>
              </ul>
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Email:</label>
              <input type="text" name="email" v-model="form.email" class="form-control" />
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password:</label>
              <input type="password" name="password" v-model="form.password" class="form-control" />
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
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
  name: 'Login',
  components: {
    HeroImage
  },
  data() {
    return {
      form: {
        email: '',
        password: '',
        errors: [],
      }
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      let router = this.$router;
      this.form.errors = [];

      if (!this.form.email) {
        this.form.errors.push('Email required.');
      }
      if (!this.form.password) {
        this.form.errors.push('Password required.');
      }
      if (this.form.errors.length > 0) {
        return false;
      }
      try {
        await this.logIn(this.form).then(
          function response() {
            router.push('/dashboard');
          }
        );
      } catch (error) {
        this.form.errors.push(error.response.data.detail);
      }
    }
  }
});
</script>