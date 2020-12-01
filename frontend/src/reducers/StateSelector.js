export function deriveLocation(selectedValue) {

    if (selectedValue == 'b') {

        return { location: 'Event', nextLocation: 'Place'}

      }
      else{

        return { location: 'Place', nextLocation: 'Event'}
      }

}

export function deriveStateFromLocation(locationObject) {

    if (locationObject.location == 'Event') {

        return 'b'

      }
      else{

        return 'c'
      }

}

export function nextState(currentState) {

    if (currentState == 'e' || currentState == 'd' ){
        return 'f'
    }

    //Place selected as level-2
    if (currentState == 'c') {
        return 'e'
    }

    //Event selected as level-2
    if (currentState == 'b') {
        return 'd'
    }

    return 'a'
}

export function stepCount (currentState) {

    if ( currentState == 'a')
        return 0

    if (currentState == 'b' || currentState == 'c' )
        return 1

    if (currentState == 'd' || currentState == 'e' )
        return 2

    return 3
}

export function isEventStep (currentState) {

    if (currentState == 'b') //
        return true

    if (currentState == 'e') //
        return true

    return false
}

export function isPlaceStep (currentState) {

    if (currentState == 'c') //
        return true

    if (currentState == 'd') //
        return true

    return false
}

export function isFirstStep (currentState) {

    if (currentState == 'a') //
        return true

    return false
}

export function isLastStep (currentState) {

    if (currentState == 'f') //
        return true

    return false
}
