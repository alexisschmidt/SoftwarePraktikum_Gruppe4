import NamedBo from "./NamedBo";

export default class ModuleTypebo extends NamedBo{

	constructor() {
		super();

	  }
	
	  
	  static fromJSON(moduletype) {
		let result = [];
	
		if (Array.isArray(moduletype)) {
			moduletype.forEach((a) => {
			Object.setPrototypeOf(a, ModuleTypebo.prototype);
			result.push(a);
		  })
		} else {
		  // Es handelt sich offenbar um ein singuläres Objekt
		  let a = moduletype;
		  Object.setPrototypeOf(a, ModuleTypebo.prototype);
		  result.push(a);
		}
	
		return result;
	  }
	}