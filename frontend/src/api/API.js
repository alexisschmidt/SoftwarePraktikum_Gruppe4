//Import BOs

export default class API{
	//Singleton instance
		static #api = null;
	
		//local Python backend
		#serverBaseURL = '/sopra';
	
		//Local http-fake-backend?
	
	
		//... related
		#getCustomersURL = () => `${this.#bankServerBaseURL}/customers`;
	
		//... related
	
		/** 
	   * Get the Singelton instance 
	   * 
	   * @public
	   */
		 static getAPI() {
			if (this.#api == null) {
			  this.#api = new BankAPI();
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