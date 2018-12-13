class Record {
  recordList(data) {
    const card = document.getElementById("cardComponent");

    const li = document.createElement("li");
    li.className = "cards__item";

    const divCard = document.createElement("div");
    divCard.className = "card";

    const divCardImage = document.createElement("div");
    divCardImage.className = "card__image card__image--river";

    const divCardContent = document.createElement("div");
    divCardContent.className = "card__content";

    const divCardTitle = document.createElement("div");
    divCardTitle.className = "card__title";
    divCardTitle.innerText = data.record_type[0];

    const pCardText = document.createElement("p");
    pCardText.className = "card__text";
    pCardText.innerText = data.comment;

    const pCardText2 = document.createElement("p");
    pCardText2.className = "card__text";
    pCardText2.innerText = data.location[0];

    const cardButton = document.createElement("button");
    cardButton.className = "btn btn--block card__btn";
    cardButton.innerText = "View more";

    card.appendChild(li);
    li.appendChild(divCard);
    divCard.appendChild(divCardImage);
    divCard.appendChild(divCardContent);
    divCardContent.appendChild(divCardTitle);
    divCardContent.appendChild(pCardText);
    divCardContent.appendChild(pCardText2);
    divCardContent.appendChild(cardButton);
    console.log(card);
  }
}

// comment: "Test comment on red flag."
// id: 2
// location: ["Nairobi, Kenya"]
// record_type: Array(1)
// 0: "red-flag"
// length: 1
// __proto__: Array(0)
// status: ["draft"]
// user_id: [3]
