import axios from 'axios';

const state = {
  trainings: null,
  training: null
};

const getters = {
  stateTrainings: state => state.trainings,
  stateTraining: state => state.training,
};

const actions = {
  async createTraining({}, training) {
    console.log(training);
    await axios.post('api/trainingResults', training);
  },
  async getTrainings({commit}) {
    let {data} = await axios.get('api/trainingResults');
    console.log(data)
    commit('setTrainings', data.trainingResults);
  },
  async viewTraining({commit}, id) {
    let {data} = await axios.get(`api/trainingResults/${id}`);
    console.log(data);
    commit('setTraining', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteTraining({}, id) {
    await axios.delete(`api/trainingResults/${id}`);
  },
  async logOutTraining({commit}) {
    commit('setTraining', null);
    commit('setTrainings', null);
  }
};

const mutations = {
  setTrainings(state, trainings){
    state.trainings = trainings;
  },
  setTraining(state, training){
    state.training = training;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};