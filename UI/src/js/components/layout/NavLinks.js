import { Component } from "../common/Components";
import { nav_links } from "../common/Selectors";

class NavLinks extends Component {
  constructor() {
    super();
    this.nav_links = nav_links();
    this.onClick = this.onClick.bind(this);
    this.resetCard = this.resetCard.bind(this);
  }
  resetCard() {
    this.nav_links.forEach(li => {
      if (li.className === "active") {
        li.className = "";
      }
    });
  }

  onClick() {
    this.nav_links.forEach(li => {
      li.addEventListener("click", a => {
        // Remove any previous active classes
        this.resetCard();
        //Adding active class
        a.target.className = "active";
      });
    });
  }
}

export default NavLinks;
