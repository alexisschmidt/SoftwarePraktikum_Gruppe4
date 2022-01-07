import Modulebo from './Modulebo';
import Modulepartbo from './Modulepartbo';
import Personbo from './Personbo';
import Semesterbo from './Semesterbo';
import Spobo from './Spobo';
import SpoElementbo from './SpoElementbo';
import StudyCoursebo from './StudyCoursebo';
import Userbo from './Userbo';

export default class API{
	//Singleton instance
		static #api = null;
	
		//local Python backend
		#serverBaseURL = '/sopra';
	
		//Local http-fake-backend?
	
		//Admin Ansicht - Neue Spo erstellen
		#getSpoURL = (id) => `${this.#serverBaseURL}/spo/${id}`; //Die ausgewählte SPO wird dem Admin angezeigt abruf durch den hash? id? oder durch einzelne module?
		#addModulepartURL = () => `${this.#serverBaseURL}/spomdulepart`; //Für den Edit-Button (Modules)
		#addModuleURL = () => `${this.#serverBaseURL}/module`; //Module hinzugügen
		#getAllModulesURL = (id) => `${this.#serverBaseURL}/allmodules/${id}` //Alle Module einer id
		#addSpoURL = () => `${this.#serverBaseURL}/spo` //Spo erstellen

		//Admin Ansicht - Liste aller SPOs
		#getAllSpoRelatedURL = (id) => `${this.#serverBaseURL}/spo/${id}`; //Alle Spos die zu einem Sudiengang gehören gelistet nach WS20, SS21...

		//Admin Ansicht - Studiengänge
		#getAllStudycoursesURL = () => `${this.#serverBaseURL}/studycourses`;

		//Studenten Ansicht - Zugeordnete SPO/Ausgewählte SPO
		
		/** 
	   * Get the Singelton instance 
	   * 
	   * @public
	   */
		 static getAPI() {
			if (this.#api == null) {
			  this.#api = new API();
			}
			return this.#api;
		  }
	
		  #fetchAdvanced = (url, init) => fetch(url, init)
		.then(res => {
		  // The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500. 
		  if (!res.ok) {
			throw Error(`${res.status} ${res.statusText}`);
		  }
		  return res.json();
		}
		)
	}