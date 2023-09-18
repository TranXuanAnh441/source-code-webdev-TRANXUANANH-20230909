import axios from 'axios';

const state = {
  models: null,
  model: null
};

const getters = {
  stateModels: state => state.models,
  stateModel: state => state.model,
};

const actions = {
  async createModel({}, model) {
    console.log(model);
    await axios.post('api/trainingModels', model);
  },
  async getModels({
    commit
  }) {
    let {
      data
    } = await axios.get('api/trainingModels');
    commit('setModels', data.trainingModels);
  },
  async searchModels({
    commit
  }, search_str) {
    let {
      data
    } = await axios.get('api/trainingModels', {
      params: {
        'search': search_str
      }
    });
    console.log(search_str);
    console.log(data);
    commit('setModels', data.trainingModels);
  },
  async viewModel({
    commit
  }, id) {
    let {
      data
    } = await axios.get(`api/trainingModels/${id}`);
    commit('setModel', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateModel({}, model) {
    await axios.patch(`api/trainingModels/${model.id}`, model.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteModel({}, id) {
    await axios.delete(`api/trainingModels/${id}`);
  },
  async logOutModel({
    commit
  }) {
    commit('setModels', null);
    commit('setModel', null);
  }
};

const mutations = {
  setModels(state, models) {
    state.models = models;
  },
  setModel(state, model) {
    state.model = model;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};