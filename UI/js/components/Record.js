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
    divCardTitle.innerText = data.record_type;

    const pCardText = document.createElement("p");
    pCardText.className = "card__text";
    pCardText.innerText = data.comment;

    const pCardText2 = document.createElement("p");
    pCardText2.className = "card__text";
    pCardText2.innerText = data.location;

    const cardBudge = document.createElement("div");
    cardBudge.className = "card__budge";
    cardBudge.innerText = data.status;

    const cardButton = document.createElement("a");
    cardButton.className = "btn btn--block card__btn";
    cardButton.setAttribute("href", `record.html?id=${data.id}`);
    cardButton.innerText = "View more";

    card.appendChild(li);
    li.appendChild(divCard);
    divCard.appendChild(divCardImage);
    divCard.appendChild(divCardContent);
    divCardContent.appendChild(divCardTitle);
    divCardContent.appendChild(pCardText);
    divCardContent.appendChild(pCardText2);
    pCardText2.appendChild(cardBudge);
    divCardContent.appendChild(cardButton);
  }

  singleRecord(data) {
    console.log(data);
    const record_div = document.getElementById("single_incident");

    const description = document.createElement("div");
    description.className = "incident__desctiption";

    const description_img = document.createElement("img");
    description_img.setAttribute(
      "src",
      "https://www.healthcareinformed.com/wp-content/uploads/bb-plugin/cache/incident-and-complaint-management.fw_-1-circle.png"
    );
    description_img.setAttribute("alt", "Incident image");

    const incident__text = document.createElement("div");
    incident__text.className = "incident__text";

    const incident__span = document.createElement("span");
    incident__span.innerText = data.title;

    const incident__budge = document.createElement("div");
    incident__budge.className = "budge";
    incident__budge.innerText = "Status: " + data.status[0];

    const incident__p = document.createElement("p");
    incident__p.className = "card__text";
    incident__p.innerText = data.comment;

    const incident__p_location = document.createElement("p");
    incident__p_location.className = "card__text_location";
    incident__p_location.innerText = data.location[0];

    const cardButton = document.createElement("a");
    cardButton.className = "btn btn--block card__btn";
    cardButton.setAttribute("href", `create-incident.html?id=${data.id}`);
    cardButton.innerText = "Edit";

    record_div.appendChild(description);
    description.appendChild(description_img);
    description.appendChild(incident__text);
    incident__text.appendChild(incident__span);
    incident__text.appendChild(incident__budge);
    incident__text.appendChild(incident__p);
    incident__text.appendChild(incident__p_location);
    incident__text.appendChild(cardButton);
  }
}
