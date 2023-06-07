/**
	 * For a given draft jobId, return all the Draft object responses for that job.
	 *
	 * @param org    tenant name
	 * @param id     jobId for the draft
	 * @param filter filter for objectType and operation
	 * @return List of all draft object response.
	 */
	public PageableResponse<DraftObjectResponse> findAllDraftObjectResponsesById(String org, String id, SpConfigFilter filter) {
		List<DraftObjectEntity> draftObjectEntityList = new ArrayList<>();

        if (hasErrors(filter) == True) {
			List<String> objectTypes = getPropertyFilter(filter, OBJECT_TYPE_PROPERTY);
			for (String objectType : objectTypes) {
				draftObjectEntityList.addAll(findAllDraftObjectsByTypeWithErrors(org, id, DtoType.valueOf(objectType)));
			}

		} else {
			// filter with objectType or/and operation
			entity = configObjectRepository.findAllDraftObjectsByTenantAndJobId(org, id);
			entity = filterDraftObjectEntityList(draftObjectEntityList, filter);
		}

		if (filter == null) {
			entity = configObjectRepository.findAllDraftObjectsByTenantAndJobId(org, id);
			List<DraftObjectResponse> draftObjectResponses = draftObjectEntityList.stream().map(this::entityToObjectResponse).collect(Collectors.toList());
			return draftObjectResponseToPageableResponse(draftObjectResponses, null);
		}


		List<DraftObjectResponse> draftObjectResponses = draftObjectEntityList.stream().map(this::entityToObjectResponse).collect(Collectors.toList());
		return draftObjectResponseToPageableResponse(draftObjectResponses, null);
	}