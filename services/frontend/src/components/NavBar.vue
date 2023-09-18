<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container">
      <img src='../assets/img/ai-logo.png'>
      <a class="navbar-brand text-info" href="/">NoCodeTrainer</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul v-if="isLoggedIn" class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/datasets">Datasets</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/models">Models</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/trainings">Trainings</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/profile">My Profile</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click="logout">Log Out</a>
          </li>
        </ul>
        <ul v-else class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/register">Register</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/login">Log In</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
  
<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NavBar',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout() {
      const router = this.$router;
      await this.$store.dispatch('logOutTraining');
      await this.$store.dispatch('logOutModel');
      await this.$store.dispatch('logOutDataset');
      await this.$store.dispatch('logOut').then(
        function(response) {
          router.push('/');
        }
      );
    }
  },
});
</script>
  
<style scoped>
a {
  cursor: pointer;
}

.navbar a:hover,
.navbar .active,
.navbar .active:focus,
.navbar li:hover>a {
  color: #47b2e4;
}
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 999;
    width: 100%;
    /* height: 100px; */
}
.text-info {
  color: #47b2e4;
}

img{
max-width: 3%;
max-height: 3%;
margin-right: 3px;
} 
/* .navbar {
  padding-top: 10px;
} */</style>