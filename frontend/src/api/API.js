import Modulepartbo from './BusinessObjects/Modulepartbo';
import Personbo from './BusinessObjects/Personbo';
import Semesterbo from './BusinessObjects/Semesterbo';
import Spobo from './BusinessObjects/Spobo';
import SpoElementbo from './BusinessObjects/SpoElementbo';
import StudyCoursebo from './BusinessObjects/StudyCoursebo';
import Userbo from './BusinessObjects/Userbo';

export default class API{
	//Singleton instance
		static #api = null;
	
		//local Python backend
		#serverBaseURL = '/sopra';
	
		//Local http-fake-backend?
	
		//Admin Ansicht - Neue Spo erstellen
		#getSpoURL = (id) => `${this.#serverBaseURL}/spo/${id}`; //Die ausgewählte SPO wird dem Admin angezeigt abruf durch den hash? id? oder durch einzelne module?
		#addModulepartURL = () => `${this.#serverBaseURL}/modulepart`; //Für den Edit-Button (Modules)
		#addModuleURL = () => `${this.#serverBaseURL}/module`; //Module hinzugügen
		#getAllModulesURL = (id) => `${this.#serverBaseURL}/module/${id}` //Alle Module einer id
		#getAllModulePartsURL = (id) => `${this.#serverBaseURL}/modulepart/${id}` //Alle Moduleparts eines Modules/Spo
		#addSpoURL = () => `${this.#serverBaseURL}/spo` //Spo erstellen

		//Admin Ansicht - Liste aller SPOs
		#getAllSpoRelatedURL = (id) => `${this.#serverBaseURL}/spos/studycourse/${id}`; //Alle Spos die zu einem Sudiengang gehören gelistet nach WS20, SS21...
		
		//Admin Ansicht - Studiengänge
		#getAllStudycoursesURL = () => `${this.#serverBaseURL}/studycourses`;
		#getAllStudycoursesByIdURL = (id) => `${this.#serverBaseURL}/studycourses/${id}`;
		#getAllModulesByIdURL = (id) => `${this.#serverBaseURL}/modules/${id}`;
		#getAllModulePartsByIdURL = (id) => `${this.#serverBaseURL}/moduleparts/${id}`;
		#getAllSemesterByIdURL = (id) => `${this.#serverBaseURL}/semesters/${id}`;
		#getAllPersonsByIdURL = (id) => `${this.#serverBaseURL}/persons/${id}`;
		#getAllSposByIdURL = (id) => `${this.#serverBaseURL}/spos/${id}`;
		#getAllUsersByIdURL = (id) => `${this.#serverBaseURL}/users/${id}`;
		
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
  		/**
   		*
   		* @public
   		*/
		getSpo(spoId) {
			return this.#fetchAdvanced(this.#getSpoURL(spoId)).then((responseJSON) => {
				let responseSpobo = Spobo.fromJSON(responseJSON)[0];
				// console.info(responseSpobo);
				return new Promise(function (resolve) {
					resolve(responseSpobo);
			  	})
			})
		}

		addModulepart(modulepartbo){
			return this.#fetchAdvanced(this.#addModulepartURL(), {
				method: 'POST',
				headers: {
					'Accept': 'application/json, text/plain',
					'Content-type': 'application/json',
				},
				body: JSON.stringify(modulepartbo)
			}).then((responseJSON) => {
				let responseModulepartbo = Modulepartbo.fromJSON(responseJSON)[0];
				return new Promise(function (resolve) {
					resolve(responseModulepartbo);
				})
			})
		}

		addModule(modulebo){
			return this.#fetchAdvanced(this.#addModuleURL(), {
				method: 'POST',
				headers: {
					'Accept': 'application/json, text/plain',
					'Content-type': 'application/json',
				},
				body: JSON.stringify(modulebo)
			}).then((responseJSON) => {
				let responseModulebo = Modulebo.fromJSON(responseJSON)[0];
				return new Promise(function (resolve) {
					resolve(responseModulebo);
				})
			})

		}

		getAllModules(){
			return this.#fetchAdvanced(this.#getAllModulesURL()).then((responseJSON) => {
				let spobos = Spobo.fromJSON(responseJSON);
				// console.info(customerBOs);
				return new Promise(function (resolve) {
					resolve(spobos);
			  	})
			})
		}

		getAllModuleParts(moduleId){
			return this.#fetchAdvanced(this.#getAllModulePartsURL(moduleId)).then((responseJSON) => {
				let responseModulepartbo = Modulepartbo.fromJSON(responseJSON)[0];
				// console.info(responseModulepartbo);
				return new Promise(function (resolve) {
					resolve(responseModulepartbo);
			  	})
			})
		}

		addSpo(spoBo){
			return this.#fetchAdvanced(this.#addSpoURL(), {
				method: 'POST',
				headers: {
				  'Accept': 'application/json, text/plain',
				  'Content-type': 'application/json',
				},
				body: JSON.stringify(spoBo)
			  }).then((responseJSON) => {
				// We always get an array of CustomerBOs.fromJSON, but only need one object
				let responseSpobo = Spobo.fromJSON(responseJSON)[0];
				// console.info(accountBOs);
				return new Promise(function (resolve) {
				  resolve(responseSpobo);
				})
			  })
		}

		async getAllSpoRelated(studyCourseId) {
			return this.#fetchAdvanced(this.#getAllSpoRelatedURL(studyCourseId));
		}

		async getAllStudycourses() {
			return this.#fetchAdvanced(this.#getAllStudycoursesURL());
		}

		async getAllStudycoursesById(studycourseId) {
			return this.#fetchAdvanced(this.#getAllStudycoursesByIdURL(studycourseId));
		}

		async getAllModulesById(moduleId) {
			return this.#fetchAdvanced(this.#getAllModulesByIdURL(moduleId));
		}

		async getAllModulePartsById(modulepartId) {
			return this.#fetchAdvanced(this.#getAllModulePartsByIdURL(modulepartId));
		}

		async getAllSemesterById(semesterId) {
			return this.#fetchAdvanced(this.#getAllSemesterByIdURL(semesterId));
		}

		async getAllPersonsById(personId) {
			return this.#fetchAdvanced(this.#getAllPersonsByIdURL(personId));
		}

		async getAllSposById(spoId) {
			return this.#fetchAdvanced(this.#getAllSposByIdURL(spoId));
		}

		async getAllUsersById(userId) {
			return this.#fetchAdvanced(this.#getAllUsersByIdURL(userId));
		}

		/**
		 * Beispiel für alexis mit json parsing 
		 
		async getAllStudycourses() {
			const apidaten = await this.#fetchAdvanced(this.#getAllStudycoursesURL());
			return Spobo.fromJSON(apidaten);
		}
		*/

	}
