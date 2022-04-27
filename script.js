var url = "./jsonFiles/russianASATtestDebris.json";
async function getData() {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
}

getData().catch((err) => console.error("error"));
