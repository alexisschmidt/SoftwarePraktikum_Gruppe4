import BusinessObject from './Businessobject';

export default class Userbo extends BusinessObject{
  /**
   * Constructs a new Userbo object with a given owner.
   * 
   * @param {*} aFirstname - the owner of this Userbo.
   * @param {*} aLastname 
   * @param {*} aEmail
   * @param {*} aGoogle_user_id
   * @param {*} aIsadmin
   */
   constructor(aFirstname, aLastname, aEmail, aGoogle_user_id, aIsadmin) {
    super();
    this.firstname = aFirstname;
	  this.lastname = aLastname;
	  this.email = aEmail;
	  this.google_user_id = aGoogle_user_id;
	  this.isadmin = aIsadmin;
  }

  /**
   * Sets the owner of this Userbo.
   * 
   * @param {*} aFirstname - the new owner of this Userbo.
   */
  setFirstname(aFirstname) {
    this.firstname = aFirstname;
  }

  /**
   * Gets the owner of this Userbo.
   */
  getFirstname() {
    return this.firstname;
  }

  /**
   * Sets the owner of this Userbo.
   * 
   * @param {*} aLastname - the new owner of this Userbo.
   */
   setLastname(aLastname) {
    this.lastname = aLastname;
  }

  /**
   * Gets the owner of this Userbo.
   */
  getLastname() {
    return this.lastname;
  }

  /**
   * Sets the owner of this Userbo.
   * 
   * @param {*} aEmail - the new owner of this Userbo.
   */
   setEmail(aEmail) {
    this.email = aEmail;
  }

  /**
   * Gets the owner of this Userbo.
   */
  getEmail() {
    return this.email;
  }

  /**
   * Sets the owner of this Userbo.
   * 
   * @param {*} aGoogle_user_id - the new owner of this Userbo.
   */
   setGoogle_user_id(aGoogle_user_id) {
    this.google_user_id = aGoogle_user_id;
  }

  /**
   * Gets the owner of this Userbo.
   */
  getGoogle_user_id() {
    return this.google_user_id;
  }

  /**
   * Sets the owner of this Userbo.
   * 
   * @param {*} aIsadmin - the new owner of this Userbo.
   */
   setIsadmin(aIsadmin) {
    this.isadmin = aIsadmin;
  }

  /**
   * Gets the owner of this Userbo.
   */
  getIsadminr() {
    return this.isadmin;
  }

  /**
   * Returns an Array of Userbo from a given JSON structure
   */
  static fromJSON(user) {
    let result = [];

    if (Array.isArray(user)) {
		user.forEach((a) => {
        Object.setPrototypeOf(a, Userbo.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = user;
      Object.setPrototypeOf(a, Userbo.prototype);
      result.push(a);
    }

    return result;
  }
}