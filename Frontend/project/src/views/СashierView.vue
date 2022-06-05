<template>
  <div>
    <h1>Касса</h1>
    <button @click="save">Начислить баллы</button>
    <h3>Списать баллы</h3>
    <qrcode-stream @decode="onDecode"></qrcode-stream>
  </div>
</template>

<script>
export default {
  name: "CashView",
  methods: {
    onDecode(result) {
      result = JSON.parse(atob(result));
      this.$store.dispatch("SPEND_POINTS", result);
    },
    save() {
      this.$store.dispatch("SAVE_POINTS");
    },
  },
  data() {
    return {
      result: "",
      option: 1,
    };
  },
};
</script>


<style scoped>
.products {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.profile {
  display: flex;
  align-items: center;
  justify-content: space-around;
  border-radius: 10px;
  padding: 10px;
  border: 1px solid lightgray;
  margin-bottom: 50px;
}

h1 {
  text-align: center;
}

.user {
  display: flex;
  align-items: center;
  width: 200px;
  justify-content: space-around;
}

h4 {
  font-size: 30px;
  margin: 0;
}

label {
  background-color: lightcoral;
  border: 1px solid red;
  color: white;
  font-size: 15px;
  border-radius: 10px;
  padding: 2px 5px 2px 10px;
  margin: 5px;
}

img {
  display: block;
  width: 50px;
  height: 50px;
  border-radius: 100%;
}
</style>
