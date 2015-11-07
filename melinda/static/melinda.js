
 
var app = angular.module('searchApp',["ui.bootstrap","ngTouch", "angucomplete-alt"]);
app.controller('searchCtrl',function($scope, $http){
/*
	$http.get('/api/nomenclature/?format=json')
		.success(function(response)	{
			$scope.autolist=response;		
		}); 
*/
	
	var commands = {
		    'search for *term':invokeSearch(term){
		    	var elem = document.getElementById("searchbox_value");
		    	elem.value = term;
		    	$scope.searchStr=term;
		    	$scope.$apply();
		    };
  	
	    	//elem.keypress();
	};
		  // Add our commands to annyang
  	annyang.addCommands(commands);

  // 	Start listening. You can call this here, or attach this call to an event, button, etc.
  	annyang.start();
  		
  		
	$scope.mydata="hello world?";
	$scope.server = "//service.oib.utah.edu:8080/infobutton-service/infoRequest?";
	$scope.orgId = "1.3.6.1.4.1.5884";
	$scope.vocab_sys = "2.16.840.1.113883.6.96";
	$scope.loadingStatus= ""; 
	$scope.url = null;
	$scope.setting = "INPATIENT";
	$scope.settingSwitch = true;
	$scope.selectedItem = null;
	
	$scope.buildURL = function(selected) {
		var req = $scope.server;
		$scope.debugmsg = selected;
		if (selected != null){
			req = req + "representedOrganization.id.root="+$scope.orgId;
			req = req + "&taskContext.c.c=PROBLISTREV";
			req = req + "&mainSearchCriteria.v.c="+selected.code_identifier;
			req = req + "&mainSearchCriteria.v.cs="+"2.16.840.1.113883.6.96";
			req = req + "&mainSearchCriteria.v.dn="+selected.display;
			req = req + "&encounter.c.c=AMB";
			req = req + "&informationRecipient=PROV";
			req = req + "&informationRecipient.languageCode.c=en";
			req = req + "&informationRecipient.healthCareProvider.c.c=200000000X";
			req = req + "&performer=PROV";
			req = req + "&performer.languageCode.c=en";
			req = req + "&performer.healthCareProvider.c.c=200000000X";
		}	
		return req;
	};
	
	
	$scope.selectTerm = function(selectedTerm) {
		if (selectedTerm) {
			$scope.selectedTerm = selectedTerm;
			$scope.selectedItem= selectedTerm;
			$scope.url = $scope.buildURL(selectedTerm.originalObject);
			
		}
	};
	
	
	$scope.openURL = function() {
		if ($scope.url) {
			window.location.href =$scope.url;
		}
	};
	
	$scope.getResults = function(selectedTerm){
		if (selectedTerm) {
			$scope.resultDisplay = [];
			$scope.feeds=[];
			$scope.loadingStatus = "Loading result. . . .";
			$scope.selectedTerm = selectedTerm;
			if (selectedTerm.url =='') {
				$http.get($scope.buildURL(selectedTerm)+"&knowledgeResponseType=application/json").success(function(data) {
	            	$scope.curResultSet = data;
	    			$scope.parseResults($scope.curResultSet)
	    			$scope.loadingStatus = "Result:";
				});
			} else{
				$scope.curResultSet = $scope.parseObject(selectedTerm)
				$scope.parseResults($scope.curResultSet)
    			$scope.loadingStatus = "Result:";
			}
			
		};
		
	};
	
	
	
	$scope.parseResults=function(resultSet){
		

		for ( var i= 0; i < resultSet.feed.length; i++) {
			
			$scope.feeds.push(
					{	title: resultSet.feed[i].title.value[0],
						entry: resultSet.feed[i].entry
					});
			
			if (resultSet.feed[i].title.value[0].search("UUHC")>= 0){
				$scope.parserFeedEntry(resultSet.feed[i])
			}
		}
	};

	
	$scope.parserFeedEntry=function(feed) {
		if (feed){
			$scope.resultDisplay = [];
			for (var j=0; j<feed.entry.length;j++){
				$scope.resultDisplay.push(
						{	title: feed.entry[0].title.value[0],
							href:feed.entry[0].link[0].href,
							updated:feed.entry[0].updated
						});
			}
		}
			
	};
	
	$scope.parseObject=function(srcTerm){
		toReturn = {
					feed:[{
					      title:{value:["UUHC"]},
					      entry:[{title:{value:[srcTerm.display]},link:[{href:srcTerm.url}],updated:null}]
						  }
					]
				};
		return toReturn;
		
	};
	
	$scope.searchboxKeyPress = function(keyEvent) {
		if (keyEvent.which == 13){
			  $scope.url = $scope.buildURL($scope.selectedItem.originalObject);
			  window.location.href=$scope.url;
		}
	};
	$scope.callback = $scope.searchboxKeyPress;
	
	$scope.$watch(function(scope){
		if (scope.selectedItem){
		return scope.selectedItem.originalObject
		}},
			$scope.getResults)
	
	$scope.togglesetting= function(){
			if ($scope.settingSwitch){
				$scope.setting = "INPATIENT";
			}
			else{
				$scope.setting = "AMBULATORY"
			}
	 };

	 $scope.getPic=function(result){
		if (result.isExclusive==true) {
			return "/static/img/uuhs-logo_small.png";
		}
	 };
});


app.directive('toggleCheckbox', function($timeout) {

    /**
     * Directive
     */
    return {
        restrict: 'A',
        transclude: true,
        replace: false,
        require: 'ngModel',
        link: function ($scope, $element, $attr, ngModel) {

            // update model from Element
            var updateModelFromElement = function() {
                // If modified
                var checked = $element.prop('checked');
                
                if (checked != ngModel.$viewValue) {
                    // Update ngModel
                    ngModel.$setViewValue(checked);
                    $scope.$apply();
                }
            };

            // Update input from Model
            var updateElementFromModel = function(newValue) {
                $element.trigger('change');
            };

            // Observe: Element changes affect Model
            $element.on('change', function() {
                updateModelFromElement();
            });

            $scope.$watch(function() {
              return ngModel.$viewValue;
            }, function(newValue) { 
              updateElementFromModel(newValue);
            }, true);

            // Initialise BootstrapToggle
            $element.bootstrapToggle();
        }
    };
});

