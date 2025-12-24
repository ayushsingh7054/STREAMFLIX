const movies = [
  "Durander Ka Burnder",
  "Shadow Of Night",
  "Code Hunter",
  "Dark Signal",
  "Neon Blood"
];

const tvShows = [
  "Broken Files",
  "City Of Lies",
  "Last Server",
  "Mind Trap"
];

const newReleases = [
  "Echo World",
  "Final Route",
  "Cyber Fall"
];

let myList = [];

function renderCards(list) {
  const content = document.getElementById("content");
  content.innerHTML = "";

  if (list.length === 0) {
    content.innerHTML = "<p>No items in My List.</p>";
    return;
  }

  list.forEach(name => {
    const card = document.createElement("div");
    card.className = "card";
    card.style.backgroundImage =
      "url(https://picsum.photos/200/300?random=" + Math.random() + ")";

    card.innerHTML = `
      <div class="like" onclick="addToList(event, '${name}')">❤</div>
      <span>${name}</span>
    `;

    card.onclick = openWatch;
    content.appendChild(card);
  });
}

function loadSection(section) {
  if (section === "home" || section === "movies") renderCards(movies);
  if (section === "tv") renderCards(tvShows);
  if (section === "new") renderCards(newReleases);

  if (section === "mylist") renderCards(myList);

  if (section === "about") {
    document.getElementById("content").innerHTML = `
      <h2>About App</h2>
      <p>This streaming app UI is created for learning & experiment.</p>
      <p><b>Founder:</b> Ayush Singh</p>
      <p><b>Developer:</b> Ayush Singh</p>
    `;
  }
}

function addToList(e, name) {
  e.stopPropagation();
  if (!myList.includes(name)) myList.push(name);
}

function openWatch() {
  document.getElementById("watchModal").style.display = "flex";
}

function closeModal() {
  document.getElementById("watchModal").style.display = "none";
}

function openPlans() {
  closeModal();
  document.getElementById("planModal").style.display = "flex";
}

function closePlans() {
  document.getElementById("planModal").style.display = "none";
}

function openQR(price) {
  closePlans();
  document.getElementById("qrModal").style.display = "flex";
}

function closeQR() {
  document.getElementById("qrModal").style.display = "none";
}

loadSection("home");
