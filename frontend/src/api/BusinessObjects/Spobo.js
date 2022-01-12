import BusinessObject from './Businessobject';

export default class Spobo extends BusinessObject{
  /**
   * Constructs a new Spobo object with a given owner.
   * 
   * @param {*} aStart_semester - the owner of this Spobo.
   * @param {*} aEnd_semester
   * @param {*} aModules
   * @param {*} aStudycourse

   */
   constructor(aStart_semester, aEnd_semester, aModules, aStudycourse) {
    super();
    this.start_semester = aStart_semester;
	  this.end_semester = aEnd_semester;
	  this.modules = aModules;
	  this.studycourse = aStudycourse;
  }

  /**
   * Sets the owner of this Spobo.
   * 
   * @param {*} aStart_semester - the new owner of this Spobo.
   */
  setStart_semester(aStart_semester) {
    this.start_semester = aStart_semester;
  }

  /**
   * Gets the owner of this Spobo.
   */
  getStart_semester() {
    return this.start_semester;
  }

  /**
   * Sets the owner of this Spobo.
   * 
   * @param {*} aEnd_semester - the new owner of this Spobo.
   */
   setEnd_semester(aEnd_semester) {
    this.end_semester = aEnd_semester;
  }

  /**
   * Gets the owner of this Spobo.
   */
  getEnd_semester() {
    return this.end_semester;
  }

  /**
   * Sets the owner of this Spobo.
   * 
   * @param {*} aModules - the new owner of this Spobo.
   */
   setModules(aModules) {
    this.modules = aModules;
  }

  /**
   * Gets the owner of this Spobo.
   */
  getModules() {
    return this.modules;
  }

  /**
   * Sets the owner of this Spobo.
   * 
   * @param {*} aStudycourse - the new owner of this Spobo.
   */
   setStudycourse(aStudycourse) {
    this.studycourse = aStudycourse;
  }

  /**
   * Gets the owner of this Spobo.
   */
  getStudycourse() {
    return this.studycourse;
  }

  /**
   * Returns an Array of Spobo from a given JSON structure
   */
  static fromJSON(spo) {
    let result = [];

    if (Array.isArray(spo)) {
      spo.forEach((a) => {
        Object.setPrototypeOf(a, Spobo.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = spo;
      Object.setPrototypeOf(a, Spobo.prototype);
      result.push(a);
    }

    return result;
  }
}