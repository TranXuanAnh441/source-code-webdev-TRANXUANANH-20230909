import axios from 'axios';

const state = {
  user: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
};

const actions = {
  async register({dispatch}, form) {
    await axios.post('api/auth/register', form);
  },
  async logIn({dispatch}, form) {
    // console.log(form)
    await axios.post('api/auth/login', form);
    await dispatch('viewMe');
  },
  async viewMe({commit}) {
    let {data} = await axios.get('api/users/me');
    // console.log(data.user);
    await commit('setUser', data.user);
  },
  async deleteUser({}, id) {
    await axios.delete(`api/auth/${id}`);
  },
  async logOut({commit}) {
    let user = null;
    await axios.get('api/auth/logout');
    commit('logout', user);
  }
};

const mutations = {
  setUser(state, user) {
    state.user = user;
  },
  logout(state, user){
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};