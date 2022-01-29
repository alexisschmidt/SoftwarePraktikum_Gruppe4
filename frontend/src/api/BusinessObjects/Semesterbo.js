import NamedBo from "./NamedBo";

export default class Semesterbo extends NamedBo{

	constructor() {
		super();

	  }
	
	  
	  static fromJSON(semester) {
		let result = [];
	
		if (Array.isArray(semester)) {
			semester.forEach((a) => {
			Object.setPrototypeOf(a, Semesterbo.prototype);
			result.push(a);
		  })
		} else {
		  // Es handelt sich offenbar um ein singuläres Objekt
		  let a = semester;
		  Object.setPrototypeOf(a, Semesterbo.prototype);
		  result.push(a);
		}
	
		return result;
	  }
	}