async function getData() {
  const response = await fetch("spacStations.json");
  const data = await response.json();
  console.log(data);
}

getData().catch((err) => console.error("rak bhim ya jesser!"));

// fetch("./spaceStations.json")
//   .then((response) => {
//     return response.json();
//   })

//   .then((jsondata) => {
//     console.log(jsondata);
//   })
//   .catch((err) => console.log("error"));
