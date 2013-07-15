/**************************************************
 * File: app.js
 *
 * Project: The Music Hookup / Epstein
 *
 * Contains the Angular controllers for the views
 **************************************************/

var myapp = angular.module( 'myapp', ['ui'] );

myapp.controller( 'controller', function ($scope) 
{
    $scope.list = ["one", "two", "three", "four", "five", "six"];
});
angular.bootstrap( document, ['myapp'] );


function FirstControl($scope)
{
	$scope.messages 	= [ { user: "John", message: "I like llamas!" }, { user: "Singer", message: "I like drugs!!" } ] ;
	$scope.agenda 		= [ { item: "8:00pm loadin" }, { item: "Show up late" }, { item: "Get wasted" }, {item: "Get kicked out of bar" } ];

	$scope.addMessage = function()
	{
		$scope.messages.push( { user: "John", message: $scope.newMsg } ); 
		$scope.newMsg = '';
	};

	$scope.addAgenda = function()
	{
		$scope.agenda.push( { item: $scope.newAgenda } );
		$scope.newAgenda = '';
	};
};


function DashboardController($scope)
{
	$scope.bands 	= [ "Bang On", "Rage of the Kumquat" ];
	$scope.news  	= [ { date: 'July 4th', message: "Got to do the thing!"}, { date: 'July 6th', message: "Got to do the other thing!"} ];
	$scope.events  	= [ { date: 'July 4th', message: "Got to do the thing!"}, { date: 'July 6th', message: "Got to do the other thing!"} ];

	$scope.addEvent = function()
	{
		$scope.messages.push( { user: "John", message: $scope.newMsg } ); 
		$scope.newMsg = '';
	};
};


function SetlisterController($scope)
{
	$scope.songs 	= [ "n/a", "Song1", "Song2", "Song3", "Song4", "Song5" ];
	$scope.rules1	= [ "never", "always", "usually", "rarely" ];
	$scope.rules2   = [ "after", "before", "next to", "set opener", "set closer" ];
};


(function()
{
	angular.module( 'ui.sortable').value('uiSortableConfig', 
	{
  		sortable: { connectWith: '.column', update: 'itemsChanged', }
	});

	this.taskboard = angular.module('taskboard', ['ui.sortable']);

	this.TaskController = function($scope) 
	{
  		$scope.changed = 'Unfortunately not';

  		$scope.board = 
  		{
    		columns: 
    		[
      			{ 	name: 'todo',
        			items: [
          			{name: 'todo 1'},
          			{name: 'todo 2'},
          			{name: 'todo 3'},
          			{name: 'todo 4'}
        			]
      			},
      			{ 
      				name: 'done',
        			items: [
          				{name: 'done 1'},
         				{name: 'done 2'}
        			]
      			},
      			{ 
      				name: 'onhold',
        			items: []
      			}
    		]
  		};

  		$scope.itemsChanged = function() 
  		{
    		$scope.changed = 'Yes, of course :)';
  		}

	};
}).call(this);



