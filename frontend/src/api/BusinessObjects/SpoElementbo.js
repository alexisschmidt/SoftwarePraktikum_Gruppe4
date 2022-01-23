import NamedBo from './NamedBo';

export default class SpoElementbo extends NamedBo{
  /**
   * Constructs a new SpoElementbo object with a given owner.
   * 
   * @param {*} aEdvnr - the owner of this SpoElementbo.
   * @param {*} aEcts
   * @param {*} aWorkload

   */
   constructor(aEdvnr, aEcts, aWorkload) {
    super();
    this.edvnr = aEdvnr;
	  this.ects = aEcts;
	  this.workload = aWorkload;
  }

  /**
   * Sets the owner of this SpoElementbo.
   * 
   * @param {*} aEdvnr - the new owner of this SpoElementbo.
   */
  setEdvnr(aEdvnr) {
    this.edvnr = aEdvnr;
  }

  /**
   * Gets the owner of this SpoElementbo.
   */
  getEdvnr() {
    return this.edvnr;
  }

  /**
   * Sets the owner of this SpoElementbo.
   * 
   * @param {*} aEcts - the new owner of this SpoElementbo.
   */
   setEcts(aEcts) {
    this.ects = aEcts;
  }

  /**
   * Gets the owner of this SpoElementbo.
   */
  getEcts() {
    return this.ects;
  }

  /**
   * Sets the owner of this SpoElementbo.
   * 
   * @param {*} aWorkload - the new owner of this SpoElementbo.
   */
   setWorkload(aWorkload) {
    this.workload = aWorkload;
  }

  /**
   * Gets the owner of this SpoElementbo.
   */
  getWorkload() {
    return this.workload;
  }

  /**
   * Returns an Array of SpoElementbo from a given JSON structure
   */
  static fromJSON(spoelement) {
    let result = [];

    if (Array.isArray(spoelement)) {
      spoelement.forEach((a) => {
        Object.setPrototypeOf(a, SpoElementbo.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = spoelement;
      Object.setPrototypeOf(a, SpoElementbo.prototype);
      result.push(a);
    }

    return result;
  }
}