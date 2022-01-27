import SpoElementbo from './SpoElementbo';

export default class Modulebo extends SpoElementbo{
  /**
   * Constructs a new Modulebo object with a given owner.
   * 
   * @param {*} aType - the owner of this Modulebo.
   * @param {*} aRequirement 
   * @param {*} aOutcome
   * @param {*} aExamtype
   * @param {*} aInstructor
   * @param {*} aModuleparts
   */
   constructor(aType, aRequirement, aOutcome, aExamtype, aInstructor, aModuleparts) {
    super();
    this.type = aType;
	  this.requirement = aRequirement;
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
   setRequirement(aRequirement) {
    this.requirement = aRequirement;
  }

  /**
   * Gets the owner of this Modulebo.
   */
  getRequirement() {
    return this.requirement;
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
   setExamtype(aExamtype) {
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