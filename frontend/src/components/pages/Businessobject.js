/**
 * Basisklasse für alle BusinessObjects, für die standardmäßig eine ID angegeben ist
 */
export default class BusinessObject {
  /**
   * The null constructor.
   */
  constructor() {
    this.id = 0;
    this.creationdate = null;
    this.createdby = null;
  }

  /**
   * Setzt ID des Businessobjekts.
   *
   * @param {*} aId - neue ID für Businessobjekt.
   */
  setID(aId) {
    this.id = aId;
  }

  setCreationdate(aCreationdate) {
    this.creationdate = aCreationdate;
  }

  setCreatedby(aCreatedby) {
    this.createdby = aCreatedby;
  }

  /**
   * Gibt die ID des Businessobjekts zurück.
   */
  getID() {
    return this.id;
  }

  getCreationdate() {
    return this.creationdate;
  }

  getCreatedby() {
    return this.createdby;
  }

  /**
   * Gibt einen representativen String des Objekts zurück.
   */
  toString() {
    let result = "";
    for (var prop in this) {
      result += prop + ": " + this[prop] + " ";
    }
    return result;
  }
}
