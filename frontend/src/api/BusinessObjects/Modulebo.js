import BusinessObject from './Businessobject';

export default class Modulebo extends BusinessObject{
  /**
   * Constructs a new Modulebo object with a given owner.
   * 
   * @param {*} aType - the owner of this Modulebo.
   * @param {*} aRequirements 
   * @param {*} aOutcome
   * @param {*} aExamtype
   * @param {*} aInstructor
   * @param {*} aModuleparts
   */
   constructor(aType, aRequirements, aOutcome, aExamtype, aInstructor, aModuleparts) {
    super();
    this.type = aType;
	  this.requirements = aRequirements;
	  this.outcome = aOutcome;
	  this.examtype = aExamtype;
	  this.instructor = aInstructor;
	  this.moduleparts = aModuleparts;
  }

  /**
   * Sets the owner of this Modulebo.
   * 
   * @param {*} aType - the new owner of this Modulebo.
   */
  setType(aType) {
    this.type = aType;
  }

  /**
   * Gets the owner of this Modulebo.
   */
  getType() {
    return this.type;
  }

  /**
   * Sets the owner of this Modulebo.
   * 
   * @param {*} aRequirements - the new owner of this Modulebo.
   */
   setRequirements(aRequirements) {
    this.requirements = aRequirements;
  }

  /**
   * Gets the owner of this Modulebo.
   */
  getRequirements() {
    return this.requirements;
  }

  /**
   * Sets the owner of this Modulebo.
   * 
   * @param {*} aOutcome - the new owner of this Modulebo.
   */
   setOutcome(aOutcome) {
    this.outcome = aOutcome;
  }

  /**
   * Gets the owner of this Modulebo.
   */
  getOutcome() {
    return this.outcome;
  }

  /**
   * Sets the owner of this Modulebo.
   * 
   * @param {*} aExamtype - the new owner of this Modulebo.
   */
   setExamype(aExamtype) {
    this.examtype = aExamtype;
  }

  /**
   * Gets the owner of this Modulebo.
   */
  getExamtype() {
    return this.examtype;
  }

  /**
   * Sets the owner of this Modulebo.
   * 
   * @param {*} aInstructor - the new owner of this Modulebo.
   */
   setInstructor(aInstructor) {
    this.instructor = aInstructor;
  }

  /**
   * Gets the owner of this Modulebo.
   */
  getInstructor() {
    return this.instructor;
  }

  /**
   * Sets the owner of this Modulebo.
   * 
   * @param {*} aModuleparts - the new owner of this Modulebo.
   */
   setModuleparts(aModuleparts) {
    this.moduleparts = aModuleparts;
  }

  /**
   * Gets the owner of this Modulebo.
   */
  getModuleparts() {
    return this.moduleparts
  }


  /**
   * Returns an Array of Modulebo from a given JSON structure
   */
  static fromJSON(module) {
    let result = [];

    if (Array.isArray(module)) {
      module.forEach((a) => {
        Object.setPrototypeOf(a, Modulebo.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = module;
      Object.setPrototypeOf(a, Modulebo.prototype);
      result.push(a);
    }

    return result;
  }
}