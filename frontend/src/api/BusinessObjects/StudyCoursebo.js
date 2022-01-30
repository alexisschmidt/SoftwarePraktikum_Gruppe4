import NamedBo from "./NamedBo";

export default class StudyCourse extends NamedBo{

	constructor() {
		super();

	  }
	
	  
	  static fromJSON(studycourse) {
		let result = [];
	
		if (Array.isArray(studycourse)) {
			studycourse.forEach((a) => {
			Object.setPrototypeOf(a, StudyCourse.prototype);
			result.push(a);
		  })
		} else {
		  // Es handelt sich offenbar um ein singuläres Objekt
		  let a = studycourse;
		  Object.setPrototypeOf(a, StudyCourse.prototype);
		  result.push(a);
		}
	
		return result;
	  }
	}