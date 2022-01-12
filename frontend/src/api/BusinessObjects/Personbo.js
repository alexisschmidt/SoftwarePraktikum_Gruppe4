import BusinessObject from './Businessobject';

export default class Personbo extends BusinessObject{
  /**
   * Constructs a new Personbo object with a given owner.
   * 
   * @param {*} aFirstname - the owner of this Personbo.
   * @param {*} aLastname 
   * @param {*} aEmail

   */
   constructor(aFirstname, aLastname, aEmail) {
    super();
    this.firstname = aFirstname;
	  this.lastname = aLastname;
	  this.email = aEmail;
  }

  /**
   * Sets the owner of this Personbo.
   * 
   * @param {*} aFirstname - the new owner of this Personbo.
   */
  setFirstname(aFirstname) {
    this.firstname = aFirstname;
  }

  /**
   * Gets the owner of this Personbo.
   */
  getFirstname() {
    return this.firstname;
  }

  /**
   * Sets the owner of this Personbo.
   * 
   * @param {*} aLastname - the new owner of this Personbo.
   */
   setLastname(aLastname) {
    this.lastname = aLastname;
  }

  /**
   * Gets the owner of this Personbo.
   */
  getLastname() {
    return this.lastname;
  }

  /**
   * Sets the owner of this Personbo.
   * 
   * @param {*} aEmail - the new owner of this Personbo.
   */
   setEmail(aEmail) {
    this.email = aEmail;
  }

  /**
   * Gets the owner of this Personbo.
   */
  getEmail() {
    return this.email;
  }

  /**
   * Returns an Array of Personbo from a given JSON structure
   */
  static fromJSON(person) {
    let result = [];

    if (Array.isArray(person)) {
      person.forEach((a) => {
        Object.setPrototypeOf(a, Personbo.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = person;
      Object.setPrototypeOf(a, Personbo.prototype);
      result.push(a);
    }

    return result;
  }
}