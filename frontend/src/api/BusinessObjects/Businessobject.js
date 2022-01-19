export default class BusinessObject {

	constructor(aId, aCreationdate) {
	  this.id = aId;
	  this._creationdate = aCreationdate //aktuelles Datum
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

	setCreationdate(aCreationdate){
		this._creationdate = aCreationdate;
	}

	getCreationdate(){
		return this._creationdate;
	}
  
	toString() {
	  let result = '';
	  for (var prop in this) {
		result += prop + ': ' + this[prop] + ' ';
	  }
	  return result;
	}
  }