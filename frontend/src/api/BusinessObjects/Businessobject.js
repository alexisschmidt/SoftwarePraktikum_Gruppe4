export default class BusinessObject {

	constructor() {
	  this.id = 0;
	  this._creationdate = datetime.date.today() //aktuelles Datum
	}
  
	/**
	 * Sets the ID of this BusinessObject.
	 * 
	 * @param {*} aId - the new ID of this BusinessObject
	 * @param {*} aCreationdate
	 */
	setID(aId) {
	  this.id = aId;
	}
  
	getID() {
	  return this.id;
	}

	setCreationdate(){
		this._creationdate = aCreationdate;
	}

	getCreationdate(){
		return this.creationdate;
	}
  
	toString() {
	  let result = '';
	  for (var prop in this) {
		result += prop + ': ' + this[prop] + ' ';
	  }
	  return result;
	}
  }