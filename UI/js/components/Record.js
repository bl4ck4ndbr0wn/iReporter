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

    record_div.appendChild(description);
    description.appendChild(description_img);
    description.appendChild(incident__text);
    incident__text.appendChild(incident__span);
    incident__text.appendChild(incident__budge);
    incident__text.appendChild(incident__p);
    incident__text.appendChild(incident__p_location);
  }

  tableItem(data) {
    const table = document.getElementById("table_body");

    const tr = document.createElement("div");
    tr.className = "tr";

    const td1 = document.createElement("div");
    td1.className = "td center";
    const span1 = document.createElement("span");
    span1.innerText = data.id;

    const td2 = document.createElement("div");
    td2.className = "td grow";
    const span2 = document.createElement("span");
    span2.innerText = data.title;

    const td3 = document.createElement("div");
    td3.className = "td grow";
    const span3 = document.createElement("span");
    span3.innerText = data.record_type;

    const td4 = document.createElement("div");
    td4.className = "td  grow";
    const span4 = document.createElement("span");
    span4.innerText = data.comment;

    const td5 = document.createElement("div");
    td5.className = "td grow end";
    const span5 = document.createElement("span");
    span5.innerText = data.status;

    const td6 = document.createElement("div");
    td6.className = "td end";

    const viewBtn = document.createElement("a");
    viewBtn.setAttribute("href", `record.html?id=${data.id}`);
    const viewicon = document.createElement("i");
    viewicon.className = "fa fa-eye";

    const td7 = document.createElement("div");
    td7.className = "td end";

    const editBtn = document.createElement("a");
    const iconedit = document.createElement("i");
    iconedit.className = "fa fa-edit";
    iconedit.setAttribute("onclick", `editIncidentRecord(${data.id})`);

    const td8 = document.createElement("div");
    td8.className = "td end";

    const deleteBtn = document.createElement("a");
    const icondelete = document.createElement("i");
    icondelete.className = "fa fa-trash";

    table.appendChild(tr);
    tr.appendChild(td1);
    td1.appendChild(span1);

    tr.appendChild(td2);
    td2.appendChild(span2);

    tr.appendChild(td3);
    td3.appendChild(span3);

    tr.appendChild(td4);
    td4.appendChild(span4);

    tr.appendChild(td5);
    td5.appendChild(span5);

    tr.appendChild(td6);
    td6.appendChild(viewBtn);
    viewBtn.appendChild(viewicon);

    tr.appendChild(td7);
    td7.appendChild(editBtn);
    editBtn.appendChild(iconedit);

    tr.appendChild(td8);
    td8.appendChild(deleteBtn);
    deleteBtn.appendChild(icondelete);
  }
}
