function concatx(array1, array2){
	for(i=0;i<array2.length;i++){
	  array1.push(array2[i]);
	}
    return array1;
}
    
    
function loadSubregionData(callback){
    d3.json("data/subregional-2.json", function(error, SRdata) {
        srData = SRdata;
        weeks = srData.weekmetadata;
        numerator = indicator1;
        denominator = indicator2;
        genData(numerator,denominator);
        callback();
    })
}

function genData(numerator,denominator){
	sub_data = genDataSubRegion(numerator, denominator,selected_subregion);
    nat_data = genDataNational(numerator, denominator)
}

function genDataSubRegion(numerator, denominator,selected_subregion){
	subregiondata = srData['data'][selected_subregion]['subregionalvals']
	// console.dir(alldata)
	metadata = srData['subRegionMetadata']
	weeks = srData['weekmetadata']

	indicatordata1 = _.pluck(subregiondata,_.indexOf(metadata, numerator))


	indicatordata2 = _.pluck(subregiondata,_.indexOf(metadata, denominator))


	var NumdataMa= new gauss.Vector(indicatordata1)
	var DendataMa= new gauss.Vector(indicatordata2)
	var sN=12;

	NumMA =NumdataMa.ema(sN).toArray()
	DenMA =DendataMa.ema(sN).toArray()

	indicatorx=[]
	for(i=0;i<NumMA.length;i++){
	    indicatorx.push(NumMA[i]/(DenMA[i]*1.0)*100.)
	}

	indicatordataOrignal = _.pluck(subregiondata,_.indexOf(metadata, 'p3'))

	ys =concatx(indicatordataOrignal.slice(0,sN-1),indicatorx);
	// console.log(ys)
	return ys;
    
}

function genDataNational(numerator, denominator){
   nationaldata = srData['nationalData']
    // console.dir(alldata)
    metadata = srData['nationalMetadata']
    weeks = srData['weekmetadata']
    indicatordata1 = _.pluck(nationaldata,_.indexOf(metadata, numerator))
    
  
    indicatordata2 = _.pluck(nationaldata,_.indexOf(metadata, denominator))
    

    var NumdataMa= new gauss.Vector(indicatordata1)
    var DendataMa= new gauss.Vector(indicatordata2)
    var sN=12;
    NumMA =NumdataMa.ema(sN).toArray()
    DenMA =DendataMa.ema(sN).toArray()
    
    indicatorx=[]
    for(i=0;i<NumMA.length;i++){
        indicatorx.push(NumMA[i]/(DenMA[i]*1.0)*100.)
    }

   
   
   indicatordataOrignal = _.pluck(nationaldata,_.indexOf(metadata, 'p3'))

    ys =concatx(indicatordataOrignal.slice(0,sN-1),indicatorx);
    // console.log(ys)
    return ys;
    
}

// var srData, selected_subregion='CENTRAL 1', indicator1='p3c',indicator2='p3b';
// loaddata()