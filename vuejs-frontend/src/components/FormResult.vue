<template>
  <h1>Home Page</h1>
  <div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">Full Name</span>
  <input type="text" class="form-control" placeholder="Full Name" aria-label="Fullname" aria-describedby="basic-addon1">
</div>
<div>
  <span style="font-size: 12px; color: blue;">Fill with numbers that range from 0.1 to 9.9</span>
</div>
<table>
  <tr>
    <td></td><td><strong>Length</strong></td><td><strong>Width</strong></td>
  </tr>
  <tr>
    <td><strong>Sepal</strong></td>
    <td>
      <input type="text" class="form-control" aria-describedby="basic-addon1">
    </td>
    <td>
      <input type="text" class="form-control" aria-describedby="basic-addon1">
    </td>
  </tr>
  <tr>
    <td><strong>Petal</strong></td>
    <td>
      <input type="text" class="form-control" aria-describedby="basic-addon1">
    </td>
    <td>
      <input type="text" class="form-control" aria-describedby="basic-addon1">
    </td>
  </tr>
  <tr>
    <td colspan="3">
      <button class="btn btn-primary" type="submit">Submit</button>
    </td>
  </tr>
</table>
<div id="v"><span>Predicted Value: </span></div>
</template>
<style scoped>
button, #v {
  padding: 6px;
  margin: 6px;
}
span {
  font-size: 28px;
}
</style>
